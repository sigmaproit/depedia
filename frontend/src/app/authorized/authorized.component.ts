import {Component, OnInit} from '@angular/core';
import {AuthService} from '../auth/auth.service';
import {Router} from '@angular/router';

@Component({
    selector: 'app-authorized',
    templateUrl: './authorized.component.html',
    styleUrls: ['./authorized.component.sass']
})
export class AuthorizedComponent implements OnInit {

    constructor(private auth: AuthService, private router: Router) {
    }

    ngOnInit() {
        this.login();
    }

    login() {
        this.auth.login().then(() => {
            this.router.navigate(['/']);
        });
    }

}
