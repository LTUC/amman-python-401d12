import React from 'react';
import ChildCat from './ChildCat';
import frankie from './assets/frankie.png';
import fluffy from './assets/fluffy.jpg';
import Row from 'react-bootstrap/Row';


class Parent extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            totalNumOfTunas : 15
        }
    }

    componentDidMount() {
        console.log("Hello");
      }

    decrementNumOfTotalTunas = () => {
        this.setState({
            totalNumOfTunas : this.state.totalNumOfTunas -1
        })
    }
    render(){
        return(
            <div>
                <h2>Parent</h2>
                <h3>Total Numbers of Tunas = {this.state.totalNumOfTunas}</h3>
                <Row xs={1} md={2} className="g-4">
                    <ChildCat 
                        name='Frankie' 
                        imgUrl={frankie} 
                        decrementTotal={this.decrementNumOfTotalTunas} />
                    
                    <ChildCat 
                        name='Fluffy' 
                        imgUrl={fluffy}
                        decrementTotal={this.decrementNumOfTotalTunas}/>

                </Row>
            </div>
        )
    }
}

export default Parent;