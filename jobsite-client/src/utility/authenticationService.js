function logout() {
    localStorage.removeItem('user');
    localStorage.removeItem('userToken');
    localStorage.removeItem('admin');
    localStorage.removeItem('adminToken');
}

function login(user, token){
    localStorage.setItem('user', JSON.stringify(user));
    localStorage.setItem('userToken', token);
}

function changeUser(user){
    localStorage.setItem('user', JSON.stringify(user));
}

function getUser() {
    return JSON.parse(localStorage.getItem('user'));
}

function getUserToken() {
    return localStorage.getItem('userToken')
}

function loginAdmin(admin, token) {
    localStorage.setItem('admin', JSON.stringify(admin));
    localStorage.setItem('adminToken', token);
}

function getAdmin() {
    return JSON.parse(localStorage.getItem('admin'));
}

function getAdminToken() {
    return localStorage.getItem('adminToken');
}

export const authenticationService = {logout, login, getUser, getUserToken, changeUser, loginAdmin, getAdmin, getAdminToken};
