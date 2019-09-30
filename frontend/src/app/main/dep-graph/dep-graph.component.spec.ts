import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DepGraphComponent } from './dep-graph.component';

describe('DepGraphComponent', () => {
  let component: DepGraphComponent;
  let fixture: ComponentFixture<DepGraphComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DepGraphComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DepGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
