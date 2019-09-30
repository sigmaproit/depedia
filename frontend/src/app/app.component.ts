import {Component, OnInit} from '@angular/core';
import {AuthService} from './auth/auth.service';
import {Router} from '@angular/router';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {

    constructor(private auth: AuthService, private router: Router) {
    }

    ngOnInit(): void {
        this.auth.isLoggedIn();
    }

}
