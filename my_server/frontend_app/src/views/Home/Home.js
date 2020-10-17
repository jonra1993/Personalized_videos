import React, { useState, useEffect } from 'react';
import useStyles from './styles'
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import AppTopBar from '../../components/AppTopBar/AppTopBar'
import axios from 'axios'

// Hooks tell React that your component needs to do something after render

export default function Home(props) {
  // Create a state spacing with default value of 2

  const [counter, setCounter] = useState(2);
  const [data, setData] = useState({ hits: [] });
  const [query, setQuery] = useState('react');

  const classes = useStyles();

  // componentDidUpdate just if counter have changed:
  useEffect(() => {
    console.log(`Counter is ${counter} `);
  }, [counter]); // Only re-run the effect if count changes


  // Similar to componentDidMount and componentDidUpdate no []:
  //  it runs both after the first render and after every update
  // effects happen “after render”
  useEffect(() => {
    // Update the document title using the browser API
    console.log('components have been updated ');
  });

  useEffect(() => {
    function handleStatusChange(status) {
      //setIsOnline(status.isOnline);
    }
    //ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    
    // Specify how to clean up after this effect as component willunmount
    return function cleanup() {
      //ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    };
  });
  
  useEffect(() => {
    let ignore = false;

    async function fetchData() {
      const result = await axios('https://hn.algolia.com/api/v1/search?query=' + query);
      if (!ignore) setData(result.data);
    }

    fetchData();
    return () => { ignore = true; }
  }, [query]);


  const incrementCounter = () => {
    setCounter(counter + 1);
  };
  const decrementCounter = () => {
    setCounter(counter - 1);
  };  

  return (
    <div className={classes.root}>
      <AppTopBar text1 = {'Hello'} text2 = {'Chao'} data = {{text1:'Hi', text2:'Ho'}}>

      </AppTopBar>
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
          <Paper className={classes.paper}>
            <input value={query} onChange={e => setQuery(e.target.value)} />
            <ul>
              {data.hits.map(item => (
                <li key={item.objectID}>
                  <a href={item.url}>{item.title}</a>
                </li>
              ))}
            </ul>
          </Paper>
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