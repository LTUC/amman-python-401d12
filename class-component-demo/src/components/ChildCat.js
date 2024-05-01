import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';



class ChildCat extends React.Component {

    constructor(props) {
        super(props); 
        this.state = {
            numOfPets : 0,
            numOfTunas: 0
        }
    }

    incrementNumOfPets = () => {
        this.setState({
            numOfPets : this.state.numOfPets + 1
        })
    }

    iNeedTuna = () => {
        this.setState({
            numOfTunas : this.state.numOfTunas +1
        })

        this.props.decrementTotal(); //to decrement total Tunas
    }

    render(){
        return(
            <Col>
                <Card style={{ width: '18rem' }}>
                    <Card.Img variant="top" src={this.props.imgUrl} onClick={this.incrementNumOfPets} />
                    <Card.Body>
                        <Card.Title>{this.props.name}</Card.Title>
                        <Card.Text>
                            <p>Num of pets 😸: {this.state.numOfPets}</p>
                            <p>Num of Tunas 🐠: {this.state.numOfTunas}</p>
                        </Card.Text>
                        <Button variant="primary" onClick={this.iNeedTuna}>I need a Tuna</Button>
                    </Card.Body>
                </Card>
            </Col>
        )
    }
}

export default ChildCat;