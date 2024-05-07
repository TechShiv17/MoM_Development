import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MinutesMeetingOutputComponent } from './minutes-meeting-output.component';

describe('MinutesMeetingOutputComponent', () => {
  let component: MinutesMeetingOutputComponent;
  let fixture: ComponentFixture<MinutesMeetingOutputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MinutesMeetingOutputComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MinutesMeetingOutputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
