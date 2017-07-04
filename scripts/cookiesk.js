/*
Sets the cookie to the set value
@param cvalue the name of the cookie
*/
function setUserCookie(account, cvalue) {
    document.cookie = account + "=" + cvalue;
}

function checkValidUser(user) {
    if (user == null || user == " " || user == "") {
        return null;
    }
    else {
        return user;
    }
}

function getUserCookie(account) {
    var type = account+"=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(type) == 0) {
            return c.substring(type.length, c.length);
        }
    }
    return "";
}