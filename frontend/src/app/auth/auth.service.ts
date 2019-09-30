import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {SERVER_BASE} from '../../const';

@Injectable({
    providedIn: 'root'
})
export class AuthService {
    user: UserModel;
    allowCredsOptions = {
        headers: {'Access-Control-Allow-Origin': '*'},
        withCredentials: true
    };

    constructor(private http: HttpClient) {
    }

    isLoggedIn() {
        if (!this.user) {
            this.checkLogin();
        }
        return !!this.user;
    }

    checkLogin() {
        this.user = JSON.parse(window.localStorage.getItem('user'));
        if (this.user) {
            this.login();
        }
    }

    login() {
        return this.http.get(`${SERVER_BASE}/user`,this.allowCredsOptions).toPromise().then((user: UserModel) => {
            this.cacheUser(user);
        }, (er) => {
            this.logout();
        });
    }

    logout() {
        this.user = null;
        window.localStorage.setItem('user', null);
    }

    updateUser(user: UserModel) {
        return this.http.post(`${SERVER_BASE}/update/user`, user, this.allowCredsOptions).toPromise().then(() => {
            this.cacheUser(user);
        });
    }

    cacheUser(user: UserModel) {
        this.user = user;
        window.localStorage.setItem('user', JSON.stringify(user));
    }
}
