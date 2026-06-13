// Packaged (Tauri) builds inject the sidecar port via eval() once the backend
// is ready: `window.__BACKEND_PORT__ = <port>`. Read it lazily at call time so
// the value is always current regardless of when eval() fires relative to page load.

const isViteDev = () => window.location.port === '5173';

export const getApiBase = () => {
  const port = window.__BACKEND_PORT__;
  if (port) return `http://127.0.0.1:${port}`;
  return isViteDev() ? 'http://localhost:8000' : '';
};

export const getWsBase = () => {
  const port = window.__BACKEND_PORT__;
  if (port) return `ws://127.0.0.1:${port}`;
  return isViteDev() ? 'ws://localhost:8000' : `ws://${window.location.host}`;
};
