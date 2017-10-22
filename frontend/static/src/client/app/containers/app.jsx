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


// class ItemList extends React.Component {
//     renderItems() {
//         return this.props.items.map(x => {
//             return (<Card
//                 name={x.name}
//                 description={x.description}
//                 key={Math.random()}
//             />);
//         });
//     }
//     render() {
//         return (<div>
//             <ul className="card-list">
//                 {this.renderItems()}
//             </ul>
//         </div>)
//     }
// }

class Home extends React.Component {
    render () {
        return <div>
            <h1>Current Offers</h1>
            {/*<ItemList*/}
                {/*items={*/}
                    {/*[*/}
                        {/*{name: 'hi', description: 'this is an item'},*/}
                        {/*{name: 'hehe', description: 'this is also an item'}*/}
                    {/*]*/}
                {/*}*/}
            {/*/>*/}
        </div>;
    }
}

// class ItemDetail extends React.Component {
//     constructor(props) {
//         super(props);
//         this.state = { pageState: 'default' };
//     }
//     setPageState(pageType) {
//         this.setState({pageState: pageType});
//     }
//     renderButtons() {
//         let pageState = this.state.pageState;
//         switch(pageState) {
//             case 'counter':
//                 return (<div>
//                     <button onClick={e => {
//                         this.setPageState('back');
//                     }}>Go Back</button>
//                     <input
//                         placeholder="Enter your counter offer">
//                     </input>
//                 </div>);
//             case 'match':
//                 return (<div>
//                     <button onClick={e => {
//                         this.setPageState('back');
//                     }}>Go Back</button>
//                     <button onClick={e => {
//                         this.setPageState('success');
//                     }}>Confirm</button>
//                 </div>);
//             case 'success':
//                 return (<div>
//                     <button onClick={e => {
//                         this.setPageState('get_key');
//                     }}>Get Key</button>
//                     <button onClick={e => {
//                         this.setPageState('confirm');
//                     }}>Profile</button>
//                 </div>);
//             default:
//                 return (<div>
//                     <button onClick={e => {
//                         this.setPageState('back');
//                     }}>Go Back</button>
//                     <button onClick={e => {
//                         this.setPageState('counter');
//                     }}>Counter</button>
//                     <button onClick={e => {
//                         this.setPageState('match');
//                     }}>Match Offer</button>
//                 </div>)
//
//         };
//         // return <div>
//         //     <button onClick={e => {
//         //         this.setPageState('back');
//         //     }}>Go Back</button>
//         //     <button onClick={e => {
//         //         this.setPageState('counter');
//         //     }}>Counter</button>
//         //     <button onClick={e => {
//         //         this.setPageState('match');
//         //     }}>Match Offer</button>
//         // </div>
//     }
//     render () {
//         const item = this.props.item;
//         return <div>
//             <h1>{`${item.name} offered by Arthas`}</h1>
//             {this.renderButtons()}
//             <div>{item.description}</div>
//         </div>;
//     }
// }


// class Card extends React.Component {
//     render() {
//         return (<div className="card">
//             <div className="card-name">
//                 {this.props.name}
//             </div>
//             <div className="card-desc">
//                 {this.props.description}
//             </div>
//         </div>);
//     }
// }

function fetchQuery(
    operation,
    variables,
) {
    return fetch('/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query: operation.text,
            variables,
        }),
    }).then(response => {
        console.log("HAHA", response);
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
                <QueryRenderer
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
                            return <Home/>;
                        } else {
                            return <div>Loading</div>;
                        }
                    }}>
                    {/*<ItemDetail*/}
                    {/*item={{name: 'lol', description: 'hello world'}}*/}
                    {/*/>*/}
                </QueryRenderer>
            </div>);
    }
}

