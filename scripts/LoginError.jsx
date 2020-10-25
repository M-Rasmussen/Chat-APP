import * as React from 'react';
import { Socket } from './Socket';
import './styles.css';



export function LoginError() {
    const [message, setMessage] = React.useState("");

    function newErrorMessage() {
        React.useEffect(() => {
            Socket.on('messageError', (data) => {
                setMessage(data['errormessage']);
            });
        });
    }

    
    newErrorMessage();
    return (
        <div>
            <p className="LoginErrorMessage"> {message} </p>
        </div>
    );
}



