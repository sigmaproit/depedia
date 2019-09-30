import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MainComponent} from './main/main.component';
import {AuthGuard} from '../auth/auth.guard';
import {ReposComponent} from './repos/repos.component';
import {DepGraphComponent} from './dep-graph/dep-graph.component';


const routes: Routes = [{
    path: 'main',
    component: MainComponent,
    canActivate: [AuthGuard],
    children: [
        {
            path: 'repos',
            component: ReposComponent
        },
        {
            path: 'graph',
            component: DepGraphComponent
        }
        ,
        {
            path: '',
            redirectTo: 'repos',
            pathMatch: 'full'
        }
    ]
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }
