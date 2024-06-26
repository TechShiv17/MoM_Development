import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ResponseModel } from 'src/models/response.model';
@Injectable({
  providedIn: 'root'
})
export class MeetingMinutesService {
  apiUrl = "http://127.0.0.1:5001/"
  constructor(private httpClient: HttpClient) { }

  convertRecording(link: string): Observable<ResponseModel> {
    const params = new HttpParams()
      .set('link', link);
    return this.httpClient.post<ResponseModel>(`${this.apiUrl}/recording-link`, {}, { params });
  }
}
