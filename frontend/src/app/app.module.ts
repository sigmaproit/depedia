import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {SignInComponent} from './sign-in/sign-in.component';
import {MatButtonModule} from '@angular/material';
import {HttpClientModule} from '@angular/common/http';
import { AuthorizedComponent } from './authorized/authorized.component';
import {MainModule} from './main/main.module';

@NgModule({
    declarations: [
        AppComponent,
        SignInComponent,
        AuthorizedComponent
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        MatButtonModule,
        HttpClientModule,
        MainModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
