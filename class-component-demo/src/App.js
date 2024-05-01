import React from 'react';
import Parent from './components/Parent';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

class App extends React.Component {
  render(){
    return(
      <>
        <Router>
          <Routes>
            <Route 
              exact path="/"
              element={<Parent />}
            >
            </Route>
          </Routes>
        </Router>
      </>
    )
  }
}

export default App;