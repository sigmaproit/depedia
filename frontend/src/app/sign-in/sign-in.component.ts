import {Component, OnInit} from '@angular/core';
import {LOGIN_URL} from '../../const';

@Component({
    selector: 'app-sign-in',
    templateUrl: './sign-in.component.html',
    styleUrls: ['./sign-in.component.sass']
})
export class SignInComponent implements OnInit {

    constructor() {
    }

    ngOnInit() {
    }

    openOauth() {
        window.location.replace(LOGIN_URL);
    }

}
