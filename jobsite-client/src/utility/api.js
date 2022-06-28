
const API_URL = 'http://localhost:8000/api'

export const post = (url, body, token = undefined) => {
  let _token
  if (token === undefined) {
    _token = token;
  } else {
    _token = `Bearer ${token}`;
  }
  return fetch(API_URL + url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      Authorization: _token,
    },
    body: JSON.stringify(body),
  }).then(
    (res) => {
      return res;
    },
    (error) => {
      console.log(error);
    }
  );
};
export const authPostMultiPart = (url, body, token) => {
  /*
  return fetch(API_URL + url, {
    method: "POST",
    headers: {
      "X-Auth-Token": token,
    },
    body: body,
  });
  */

  const _token = `Bearer ${token}`;
  return fetch(API_URL + url, {
    method: "POST",
    headers: {
      Authorization: _token,
    },
    body: body,
  }).then(
    (res) => {
      if (!res.ok) {
        if (res.status === 401) {
          throw Error("Unauthorized");
        } else {
          console.log(res);
          try {
            res.json().then((res1) => console.log(res1));
          } catch (err) {}
          throw Error();
        }
      }
      return res.json();
    },
    (error) => {
      console.log(error);
    }
  );
};
export const authPut = (url, body, token) => {
  const _token = `Bearer ${token}`;
  return fetch(API_URL + url, {
    method: "PUT",
    headers: {
      "content-type": "application/json",
      Authorization: _token,
    },
    body: JSON.stringify(body),
  });
};

export const get = (url, token = undefined) => {
  let _token
  if (token === undefined) {
    _token = token;
  } else {
    _token = `Bearer ${token}`;
  }
  return fetch(API_URL + url, {
    method: "GET",
    headers: {
      "content-type": "application/json",
      Authorization: _token,
    },
  }).then(
    (res) => {
      if (!res.ok) {
        if (res.status === 401) {
          throw Error("Unauthorized");
        } else {
          console.log(res);
          try {
            res.json().then((res1) => console.log(res1));
          } catch (err) {}
          throw Error();
        }
      }
      return res.json();
    },
    (error) => {
      console.log(error);
    }
  );
};
export const authDelete = (url, body, token) => {
  const _token = `Bearer ${token}`;
  return fetch(API_URL + url, {
    method: "DELETE",
    headers: {
      "content-type": "application/json",
      Authorization: _token,
    },
    body: JSON.stringify(body),
  }).then(
    (res) => {
      if (!res.ok) {
        if (res.status === 401) {
          throw Error("Unauthorized");
        } else {
          console.log(res);
          try {
            res.json().then((res1) => console.log(res1));
          } catch (err) {}
          throw Error();
        }
      }
      return res.json();
    },
    (error) => {
      console.log(error);
    }
  );
};

