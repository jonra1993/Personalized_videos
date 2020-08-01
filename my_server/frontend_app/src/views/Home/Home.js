import React, { useState, useEffect } from 'react';
import useStyles from './styles'
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import axios from 'axios'

export default function Home(props) {
  // Create a state spacing with default value of 2

  const [counter, setCounter] = useState(2);
  const [data, loadData] = useState(null)

  const classes = useStyles();

  // componentDidUpdate just if counter have changed:
  useEffect(() => {
    console.log(`Counter is ${counter} `);
  }, [counter]); // Only re-run the effect if count changes


  // Similar to componentDidMount and componentDidUpdate no []:
  //useEffect(() => {
    // Update the document title using the browser API
  //  document.title = `You clicked ${count} times`;
  //});

  // similar to  componentDidMount(), after first render []
  useEffect(() => {
    async function fetchData(){
      let listItems = await axios(
        'GET https://od-api-demo.oxforddictionaries.com:443/api/v1/domains/en/es'
      )
      loadData(listItems.data)
      console.log('hello')
      console.log(listItems.data)
    }
    fetchData();
  }, [])

  const incrementCounter = () => {
    setCounter(counter + 1);
  };
  const decrementCounter = () => {
    setCounter(counter - 1);
  };  

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>xs=12</Paper>
        </Grid>
        <Grid item xs={6}>
          <Paper className={classes.paper}>xs=6</Paper>
        </Grid>
        <Grid item xs={6}>
          <Paper className={classes.paper}>xs=6</Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper className={classes.paper}>xs=3</Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper className={classes.paper}>
            <Button
              variant="contained"
              color="primary"
              className={classes.button}
              startIcon={<ArrowDownwardIcon/>}
              onClick={decrementCounter}
            >
              Decrease
            </Button>            
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper className={classes.paper}>
            {counter}
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper className={classes.paper}>
            <IconButton color="primary" aria-label="increase counter" component="span" onClick={incrementCounter}>
              <ArrowUpwardIcon />
            </IconButton>            
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}