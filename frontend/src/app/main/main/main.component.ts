import { Component, OnInit } from '@angular/core';
import {AuthService} from '../../auth/auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.sass']
})
export class MainComponent implements OnInit {
    username;

  constructor(private authSvc: AuthService, private router: Router) { }

  ngOnInit() {
      this.username = this.authSvc.user.login;
  }

  logout() {
      this.authSvc.logout();
      this.router.navigate(['/welcome']);
  }

}
