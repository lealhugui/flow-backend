
/* Login e User */
export const GET_CURR_USER = 'GET_CURR_USER';
export function actGetCurrUser(){
    return { type: GET_CURR_USER };
}

export const DO_LOGIN = 'DO_LOGIN';
export function actDoLogin(username, pass){
    return {
        type: DO_LOGIN,
        user: username,
        password: pass
    };
}