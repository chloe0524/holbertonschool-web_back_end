/* eslint-disable */
import Building from './5-building.js';

function createSkyHighBuilding(sqft, floors) {
    const building = new Building(sqft);
    return {
    ...building,
    _floors: floors,
    get sqft() {
      return building.sqft;
    },
    get floors() {
      return this._floors;
    },
    evacuationWarningMessage() {
      return `Evacuate slowly the ${this._floors} floors.`;
    }
  };
}

export default createSkyHighBuilding;