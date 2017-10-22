import React from 'react';
import {range, map} from 'lodash';

class ItemList extends React.Component {
    renderItems() {
        return this.props.items.map(x => {
            return (<Card
                img={x.img}
                name={x.name}
                price={x.price}
                owner={x.owner}
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
        return (
            <div>
                <header>
                    <div className="title">༼ つ ◕_◕ ༽つ GET PWNIT ༼ つ ◕_◕ ༽つ</div>
                </header>

                <div>
                    <h1>Current Offers</h1>
                    <ItemList
                        items={map(range(55), function(i){
                            let n=i%3;
                                if (n===0) {
                                    return {
                                        img: 'https://c2.staticflickr.com/6/5322/17413647719_5110a79f16_b.jpg',
                                        name: 'Badlands 2',
                                        price: '$30',
                                        owner: 'Jerry Seinfeld'
                                    };
                                } else if (n===1) {
                                    return {
                                        img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Civ1_logo_v1.svg/1600px-Civ1_logo_v1.svg.png',
                                        name: 'Civilizations V',
                                        price: '$15',
                                        owner: 'Dave Chappelle'
                                    };

                                } else {
                                    return {
                                        img: 'http://www.gamerheadlines.com/wp-content/uploads/2014/09/Middle-Earth-Shadow-of-Mordor-724x334-1.jpg',
                                        name: 'Shadows of Mordor',
                                        price: '$55',
                                        owner: 'Dave Chappelle'
                                    };
                                }
                        })}
                    />
                </div>
            </div>
        );
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
                        placeholder="Enter counter offer">
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
        // return <div>
        //     <button onClick={e => {
        //         this.setPageState('back');
        //     }}>Go Back</button>
        //     <button onClick={e => {
        //         this.setPageState('counter');
        //     }}>Counter</button>
        //     <button onClick={e => {
        //         this.setPageState('match');
        //     }}>Match Offer</button>
        // </div>
    }
    render () {
        const item = this.props.item;
        return (
            <div>
                <header>
                    <div className="title">༼ つ ◕_◕ ༽つ GET PWNIT ༼ つ ◕_◕ ༽つ</div>
                </header>

                {this.renderButtons()}

                <div className="item-detail">
                    {/*<div className="item-img"><img src={item.img} width="150"/></div>*/}
                    <div className="item-img"><img src="https://c2.staticflickr.com/6/5322/17413647719_5110a79f16_b.jpg" width="400"/></div>
                    <div className="item-status">
                        Latest Bid: $55
                    </div>
                    <div className="item-name">
                        <h1>{item.name}</h1>
                    </div>
                    <div>Starting Price: {item.price}</div>
                </div>
                {this.renderButtons()}
            </div>
                )
    }
}


class Card extends React.Component {
    render() {
        return (
            <div className="card">
                <div className="card-img">
                    <img src={this.props.img} width="100"/>
                </div>
                <div className="subtitle">
                    <div className="card-name">
                        <a href="/#/cards/id" title={this.props.name}>{this.props.name}</a>
                    </div>
                    <div className="card-price">
                        {this.props.price}
                    </div>
                    {/*<div className="card-owner">*/}
                        {/*<a href="/#/users/id" title={this.props.owner}>{this.props.owner}</a>*/}
                    {/*</div>*/}
                </div>
            </div>);
    }
}

export default class App extends React.Component {
    render () {
        return (<div className="app-container">
            {/*<Home/>*/}
            <ItemDetail
                item={{name: 'Badlands 2', price: '$30'}}
            />
        </div>);
    }
}

