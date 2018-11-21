import { isDebugMode } from '@/modules/utils';
import { mockCharacters } from '@/modules/mockData';
export class DndApi {
  constructor (baseUrl = '') {
    this._baseUrl = baseUrl;
  }

  generateUrl (path = '') {
    return [this._baseUrl, path].join('');
  }

  _getJson (url = '') {
    return fetch(url).then(res => res.json());
  }

  // warn developers that mock data is being returned
  async _checkParamsForMock (params, url) {
    if (typeof params === 'object' && params.isMock) {
      console.warn('using mock data for API call', url);
      await this._mockDelay();
    }
  }

  _mockDelay (length = 1000) {
    console.warn('using a mock delay (ms):', length);
    return new Promise(fulfill => setTimeout(fulfill, length));
  }

  _objectToUrlParams (params = {}) {
    // assumption: each value is a string or easily converted into a string
    return Object.keys(params)
      .map(key => `${key}=${params[key]}`)
      .join('&');
  }

  _toApiUrl (url = '', params = {}) {
    return [
      url,
      this._objectToUrlParams(params),
    ].filter(v => v) // filter out empty strings
    .join('?');
  }

  async getAllCharacters (params = {}) {
    const apiUrl = this._toApiUrl('/api/character', params);
    await this._checkParamsForMock(params, apiUrl);
    return !params.isMock
      ? this._getJson(this.generateUrl(apiUrl))
      : Promise.resolve(mockCharacters.slice());
  }

  async getSingleCharacter (id, params = {}) {
    const apiUrl = this._toApiUrl(`/api/character/${id}`, params);
    await this._checkParamsForMock(params, apiUrl);
    return !params.isMock
      ? this._getJson(this.generateUrl(apiUrl))
      : Promise.resolve(mockCharacters.find(c => c.id === id));
  }
}

// use localhost for dev purposes, current domain for production
// TODO: make dev url and port configurable?
export default new DndApi(isDebugMode() ? 'http://localhost:5000' : '');
