import { Component } from '@angular/core';
import { MeetingMinutesService } from '../services/meeting-minutes.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { ResponseModel } from 'src/models/response.model';

@Component({
  selector: 'app-meeting-recording',
  templateUrl: './meeting-recording.component.html',
  styleUrls: ['./meeting-recording.component.scss']
})
export class MeetingRecordingComponent {
  isLoading: boolean = false;
  constructor(private meetingMinutesService: MeetingMinutesService, private router: Router) { }

  processLink(linkInput: string) {
    if (linkInput) {
      this.isLoading = true;
      this.meetingMinutesService.convertRecording(linkInput).subscribe(
        (response) => {
          if (response.status_code === 200) {
            this.isLoading = false;
            Swal.fire({
              title: 'Success!',
              text: 'MoM was generated successfully. Kindly check your email for generated MoM PDF.',
              icon: 'success',
            }).then((result) => {
              if (result.isConfirmed) {
                this.router.navigate(["pdf-generated"])
              }
            });
          }
        },
        (error) => {
          console.error('POST request failed!', error);
        }
      );
    }
  }

}
