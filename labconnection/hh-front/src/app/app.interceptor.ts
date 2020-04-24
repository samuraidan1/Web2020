import { HttpRequest, HttpInterceptor, HttpHandler, HttpEvent, HttpResponse, HttpErrorResponse } from '@angular/common/http'
import { Injectable } from '@angular/core'
import { Observable } from 'rxjs'

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor() {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {

    const token = localStorage.getItem('token')
    if(token) {
        console.log('done')
        const authReq = req.clone({
            headers: req.headers.set('Authorization', 'JWT ' + token )
          })
        return next.handle(authReq)
    }
    console.log('failed')
    return next.handle(req)
  }
}