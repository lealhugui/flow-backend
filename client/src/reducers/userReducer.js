import {
    GET_CURR_USER,
    DO_LOGIN
} from '../actionTypes';

function rdcUser(state={}, action){
    switch(action.type){
        case GET_CURR_USER:
            return state;
        case DO_LOGIN:
            return state;
        default:
            return state;
    }
}

export default rdcUser;