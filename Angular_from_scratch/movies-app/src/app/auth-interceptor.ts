import { HttpInterceptorFn } from '@angular/common/http';
// ng generate interceptor auth

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  // step1 to get token from local
  const token = localStorage.getItem('access_token');
  //step 2 inject the token into header
  if (token) {
    const cloned = req.clone(
      {
        setHeaders: {
          Authorization: `Bearer ${token}`
        }
      }
    )
      // step3 proceed with request
    return next(cloned);
  }

  return next(req);
};
