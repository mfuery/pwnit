import React from 'react';
import {
    QueryRenderer,
    graphql,
} from 'react-relay';
import {
    Environment,
    Network,
    RecordSource,
    Store,
} from 'relay-runtime';


class ItemList extends React.Component {
    renderItems() {
        return this.props.items.map(x => {
            return (<Card
                name={x.node.name}
                // description={x.node.description}
                key={Math.random()}
            />);
        });
    }
    render() {
        return (<div>
            <ul className="card-list">
                {this.renderItems()}
            </ul>
        </div>)
    }
}

class Home extends React.Component {
    render () {
        return <QueryRenderer
            environment={modernEnvironment}
            // operations={{}}
            // variables={{}}
            query={graphql`
                        query AllItemsQuery {
                            allItems(first: 1) {
                                edges {
                                    node {
                                        id
                                        name
                                    }
                                }
                            }
                          }
                    `}
            render={({error, props}) => {
                if (props) {
                    let items = props.allItems.edges;
                    return <div>
                        <h1>Current Offers</h1>
                        <ItemList
                            items={items}
                        />
                    </div>
                } else {
                    return <div>Loading</div>;
                }
            }}>
            {/*<ItemDetail*/}
            {/*item={{name: 'lol', description: 'hello world'}}*/}
            {/*/>*/}
        </QueryRenderer>;
    }
}

class ItemDetail extends React.Component {
    constructor(props) {
        super(props);
        this.state = { pageState: 'default' };
    }
    setPageState(pageType) {
        this.setState({pageState: pageType});
    }
    renderButtons() {
        let pageState = this.state.pageState;
        switch(pageState) {
            case 'counter':
                return (<div>
                    <button onClick={e => {
                        this.setPageState('back');
                    }}>Go Back</button>
                    <input
                        placeholder="Enter your counter offer">
                    </input>
                </div>);
            case 'match':
                return (<div>
                    <button onClick={e => {
                        this.setPageState('back');
                    }}>Go Back</button>
                    <button onClick={e => {
                        this.setPageState('success');
                    }}>Confirm</button>
                </div>);
            case 'success':
                return (<div>
                    <button onClick={e => {
                        this.setPageState('get_key');
                    }}>Get Key</button>
                    <button onClick={e => {
                        this.setPageState('confirm');
                    }}>Profile</button>
                </div>);
            default:
                return (<div>
                    <button onClick={e => {
                        this.setPageState('back');
                    }}>Go Back</button>
                    <button onClick={e => {
                        this.setPageState('counter');
                    }}>Counter</button>
                    <button onClick={e => {
                        this.setPageState('match');
                    }}>Match Offer</button>
                </div>)

        };
        return <div>
            <button onClick={e => {
                this.setPageState('back');
            }}>Go Back</button>
            <button onClick={e => {
                this.setPageState('counter');
            }}>Counter</button>
            <button onClick={e => {
                this.setPageState('match');
            }}>Match Offer</button>
        </div>
    }
    render () {
        const item = this.props.item;
        return <div>
            <h1>{`${item.name} offered by Arthas`}</h1>
            {this.renderButtons()}
            <div>{item.description}</div>
        </div>;
    }
}


class Card extends React.Component {
    render() {
        return (<div className="card">
            <div className="card-name">
                {this.props.name}
            </div>
            {/*<div className="card-desc">*/}
            {/*{this.props.description}*/}
            {/*</div>*/}
        </div>);
    }
}

function fetchQuery(
    operation,
    variables,
) {
    return fetch('/graphql', {
        method: 'POST',
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            'Content-Type': 'application/json',
        },
        credentials: "same-origin",
        body: JSON.stringify({
            query: operation.text,
            variables,
        }),
    }).then(response => {
        return response.json();
    });
}

const modernEnvironment = new Environment({
    network: Network.create(fetchQuery),
    store: new Store(new RecordSource()),
});

export default class App extends React.Component {
    render () {
        return (
            <div className="app-container">
                <Home/>
            </div>);
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
