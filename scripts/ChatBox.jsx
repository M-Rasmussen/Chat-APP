    
import * as React from 'react';
import './styles.css';

import { Socket } from './Socket';

export function ChatList(){

const [messages, setMessages] = React.useState([]);

     function getNewMessages() {
        React.useEffect(() => {
            Socket.on('message received', (data) => {
                setMessages(data['allMessages']);
            });
        });
    }

getNewMessages();

function checkSender(messaged){
    if (messaged.startsWith("bot:")){
        return('botsender');
    }
    return('userSender');
}
function checkUrlPic(messaged){
    if(messaged.includes('<ahref=')|| messaged.includes('<imgsrc=')){
        var arrOfMess=messaged.split(' ');
            var i;
            var rtnMessageInfront=" ";
            var rtnMessageBack=" ";
            var flag=true;
            var imglink;
            var pic=true;
            for(i=0; i<arrOfMess.length; i++){
                if(arrOfMess[i].includes('<ahref=')){
             
                    imglink=arrOfMess[i].slice(7); 
                    flag=false;
                    pic=false;
                    i++;
                }
                if(arrOfMess[i].includes('<imgsrc=')){
                    imglink=arrOfMess[i].slice(8);
            
                    i++;
                    flag=false;
                    pic=true;
                }
                if(flag){
                   rtnMessageInfront =rtnMessageInfront.concat(arrOfMess[i]," ");
                }else{
                   rtnMessageBack =rtnMessageBack.concat(arrOfMess[i], " ");
                }
        }
        if (pic){
        
        return(React.createElement("span", null, rtnMessageInfront,React.createElement("img",{src:imglink}),rtnMessageBack));
            
        }else{
    //console.log(rtnMessageInfront);
        return(React.createElement("span",null, rtnMessageInfront,React.createElement("a",{href:imglink}, imglink),rtnMessageBack));

        }

    }else{
        return(<div><p>{messaged}</p></div>);
    }
    
}
    
    return (
        <div className="grid-item chatgrid">
            <ul>
               {messages.map((message, index) =>
                    
                        <li key={index} className={checkSender(message)}>{checkUrlPic(message)}</li>)}
            </ul>
        </div>
        );
}