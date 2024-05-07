import { Component, OnInit } from '@angular/core';
import { MeetingMinutesService } from '../services/meeting-minutes.service';
@Component({
  selector: 'app-minutes-meeting-output',
  templateUrl: './minutes-meeting-output.component.html',
  styleUrls: ['./minutes-meeting-output.component.scss']
})
export class MinutesMeetingOutputComponent implements OnInit {

  constructor(private meetingMinutesService: MeetingMinutesService) { }

  ngOnInit(): void {
  }
  downloadPDF() {
    this.meetingMinutesService.downloadPDF()
  }
}
