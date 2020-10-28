/* botton */
import React, { useState } from 'react';
import { Socket } from './Socket';
import './styles.css';


export function Button() {
    const [message, setMessage] = useState("");
    function handleSubmit(event) {
        event.preventDefault();
        Socket.emit('new message',{
            'message' : {message},
        });
    
    console.log('Sent a message ' + { message } + ' to server!');
    setMessage("");
}
    function changed(event) {
        setMessage(event.target.value);
            }

    return (
         <div className="grid-item formwrappergrid">
        <form onSubmit={handleSubmit}>
            <div className="grid-item namegrid"></div>
            <input className="grid-item inputgrid" type="text"value={message} onChange={changed} placeholder="enter message" required/>
            <button className="grid-item submitgrid" type = "submit">Send</button>
        </form>
        </div>

    );
}
