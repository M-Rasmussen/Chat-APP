    
import * as React from 'react';
import './styles.css';

import { Button } from './Button';
import { Socket } from './Socket';
import { ChatList } from './ChatBox';
import { OnLine } from './Login';
export function Content() {


    return (
        <div className ="grid-container">
            <OnLine />
            <ChatList />
            <Button />
        </div>
    );
}
