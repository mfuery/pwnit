import React from 'react';


class ItemList extends React.Component {
    renderItems() {
        return this.props.items.map(x => {
            return (<Card
                name={x.name}
                description={x.description}
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
        return <div>
            <h1>Current Offers</h1>
            <ItemList
                items={
                    [
                        {name: 'hi', description: 'this is an item'},
                        {name: 'hehe', description: 'this is also an item'}
                    ]
                }
            />
        </div>;
    }
}

class Card extends React.Component {
    render() {
        return (<div className="card">
            <div className="card-name">
            {this.props.name}
            </div>
            <div className="card-desc">
            {this.props.description}
            </div>
        </div>);
    }
}

export default class App extends React.Component {
  render () {
    return (<div className="app-container">
        <Home/>
    </div>);
  }
}

