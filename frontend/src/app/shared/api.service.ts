import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {SERVER_BASE} from '../../const';

@Injectable({
    providedIn: 'root'
})
export class ApiService {
    allowCredsOptions = {
        headers: {'Access-Control-Allow-Origin': '*'},
        withCredentials: true
    };

    constructor(private http: HttpClient) {
    }

    listRepos() {
        return this.http.get(`${SERVER_BASE}/user/repos`, this.allowCredsOptions).toPromise();
    }

    saveRepoDependency(dep: Dependency) {
        return this.http.post(`${SERVER_BASE}/update/api_url`, dep, this.allowCredsOptions).toPromise();
    }

    getDepGraph() {
        return this.http.get(`${SERVER_BASE}/graph`, this.allowCredsOptions).toPromise();
    }

    updateRepo(data: Repo) {
        return this.http.post(`${SERVER_BASE}/update/repo`, data, this.allowCredsOptions).toPromise();
    }
}
