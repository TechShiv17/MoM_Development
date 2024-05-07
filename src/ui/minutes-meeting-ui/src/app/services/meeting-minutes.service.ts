import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class MeetingMinutesService {
  apiUrl = "http://127.0.0.1:5000/"
  constructor(private httpClient: HttpClient) { }

  convertRecording(link: string): Observable<any[]> {
    const params = new HttpParams()
      .set('link', link);
    return this.httpClient.post<any[]>(`${this.apiUrl}/recording-link`, {}, { params });
  }

  downloadPDF() {

    console.log("request send to backend to download the pdf")
  }
}
