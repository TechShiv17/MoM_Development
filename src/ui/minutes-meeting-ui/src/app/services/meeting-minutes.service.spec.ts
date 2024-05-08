import { TestBed } from '@angular/core/testing';

import { MeetingMinutesService } from './meeting-minutes.service';

describe('MeetingMinutesService', () => {
  let service: MeetingMinutesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MeetingMinutesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
