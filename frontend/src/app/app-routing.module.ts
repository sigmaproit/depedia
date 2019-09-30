import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AuthorizedComponent} from './authorized/authorized.component';
import {SignInComponent} from './sign-in/sign-in.component';


const routes: Routes = [
    {
        path: 'authorized',
        component: AuthorizedComponent
    },
    {
        path: 'welcome',
        component: SignInComponent
    },
    {
        path: '',
        redirectTo: '/main/repos',
        pathMatch: 'full'
    }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
