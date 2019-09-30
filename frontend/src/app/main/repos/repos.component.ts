import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../shared/api.service';
import {AuthService} from '../../auth/auth.service';

@Component({
  selector: 'app-repos',
  templateUrl: './repos.component.html',
  styleUrls: ['./repos.component.sass']
})
export class ReposComponent implements OnInit {
    repoList: Repo[];
    user: UserModel;
    repoApiSaved = false;
    defaultRepoApiSaved = false;
    defaultUserApiSaved = false;

  constructor(private apiSvc: ApiService, private auth: AuthService) { }

  ngOnInit() {
      this.getUser();
      this.loadRepos();
  }

  getUser() {
      this.user = this.auth.user;
  }

  loadRepos() {
      this.apiSvc.listRepos().then((repos: Repo[]) => {
          this.repoList = repos;
      });
  }

  saveDep(dep: Dependency) {
      this.apiSvc.saveRepoDependency(dep).then(() => {
          this.repoApiSaved = true;
          setTimeout(() => {
              this.repoApiSaved = false;
          }, 8000);
      });
  }

  saveRepoDefaultAPI(repo: Repo) {
      this.apiSvc.updateRepo(repo).then(() => {
          this.defaultRepoApiSaved = true;
          setTimeout(() => {
              this.defaultRepoApiSaved = false;
          }, 8000);
      });
  }

  saveUserDefaultAPI() {
      this.auth.updateUser(this.user).then(() => {
          this.defaultUserApiSaved = true;
          setTimeout(() => {
              this.defaultUserApiSaved = false;
          }, 8000);
      });
  }

}
