import React from 'react';
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom'
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

import {range, map} from 'lodash';

class ItemList extends React.Component {
    renderItems() {
        return this.props.items.map(x => {
            return (
                <Card
                    id={x.node.id}
                    name={x.node.name}
                    // description={x.node.description}
                    key={x.node.id}
                    img={'https://c2.staticflickr.com/6/5322/17413647719_5110a79f16_b.jpg'}
                />
            );
            // return (<Card
            //     img={x.img}
            //     name={x.name}
            //     price={x.price}
            //     owner={x.owner}
            //     key={Math.random()}
            // />);
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
                        <header>
                            <div className="title">༼ つ ◕_◕ ༽つ GET PWNIT ༼ つ ◕_◕ ༽つ</div>
                        </header>
                        <h1>Current Offers</h1>
                        <ItemList
                            items={items}
                        />
                    </div>
                } else {
                    return <div>Loading</div>;
                }
            }}>
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
                    <Link to={'/'}><button>Go Back</button>
                    <input
                        placeholder="Enter counter offer">
                    </input>
                    </Link>
                </div>);
            case 'match':
                return (<div>
                    <Link to={'/'}><button>Go Back</button></Link>
                    <Link to={'/confirm'}><button>Confirm</button></Link>
                </div>);
            default:
                return (<div>
                    <Link to={'/'}><button>Go Back</button></Link>
                    <Link to={'/counter'}><button>Counter Offer</button></Link>
                    <Link to={'/match'}><button>Match Offer</button></Link>
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
        const item = this.props.match.params;
        return <QueryRenderer
            environment={modernEnvironment}
            // operations={{}}
            variables={{
                id: item.id
            }}
            query={graphql`
                        query ItemQuery {
                            item(id: $id) {
                                id
                                name
                            }
                        }
                    `}
            render={({error, props}) => {
                if (props) {
                    // let items = props.allItems.edges;
                    const item = props.item;
                    return <div className="item-detail">
                        <h1>{`${item.name} offered by Arthas`}</h1>
                        {this.renderButtons()}
                        <div>{item.description}</div>
                    </div>;
                } else {
                    return <div>Loading</div>;
                }
            }}>
        </QueryRenderer>;

    }
}


class Card extends React.Component {
    render() {
        return (<Link
                to={`/item/${this.props.id}`}
            >
            <div className="card">
            <div className="card-name">
                {this.props.name}
            </div>
            <div className="card-img">
                <img src={this.props.img} width="100"/>
            </div>
            {/*<div className="card-desc">*/}
            {/*{this.props.description}*/}
            {/*</div>*/}
            </div></Link>);
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
                <Switch>
                    <Route exact path='/' component={Home}/>
                    <Route path='/item/:id' component={ItemDetail}/>
                </Switch>
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
