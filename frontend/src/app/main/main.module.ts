import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MainRoutingModule } from './main-routing.module';
import { MainComponent } from './main/main.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import { ReposComponent } from './repos/repos.component';
import {SharedModule} from '../shared/shared.module';
import {
    MatBadgeModule,
    MatButtonModule, MatCardModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatListModule, MatMenuModule
} from '@angular/material';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FlexLayoutModule} from '@angular/flex-layout';
import {FormsModule} from '@angular/forms';
import { DepGraphComponent } from './dep-graph/dep-graph.component';


@NgModule({
  declarations: [MainComponent, ReposComponent, DepGraphComponent],
    imports: [
        CommonModule,
        MainRoutingModule,
        MatToolbarModule,
        SharedModule,
        MatListModule,
        MatExpansionModule,
        MatIconModule,
        MatBadgeModule,
        BrowserAnimationsModule,
        MatFormFieldModule,
        MatInputModule,
        MatButtonModule,
        FlexLayoutModule,
        MatMenuModule,
        FormsModule,
        MatCardModule
    ]
})
export class MainModule { }
