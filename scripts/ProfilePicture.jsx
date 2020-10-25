import * as React from 'react';
import { Socket } from './Socket';
import './styles.css';



export function UserPicture() {
    const [pofilepic, setpofilepic] = React.useState("");

    function newProfilePic() {
        React.useEffect(() => {
            Socket.on('profilePic', (data) => {
                setpofilepic(data['profPicture']);
            });
        });
    }

    
    newProfilePic();
    return (
        <div>
            <img src={pofilepic} /> 
        </div>
    );
}
