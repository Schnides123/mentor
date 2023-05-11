import axios from 'axios';

const sendQuery = async (prompt, callback) => {
    const uri = process.env.REACT_APP_BACKEND_URI || 'http://127.0.0.1:5000';
    axios.get(uri, { params: { prompt: prompt } })
      .then( response => {
        console.log({ message: response.data.message, sender: "bot" });
        callback(response.data.message);
      } ).catch( ( error ) => {
        console.log( error );
      } )
}


export default sendQuery;