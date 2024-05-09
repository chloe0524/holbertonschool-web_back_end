/* eslint-disable */
import Building from './5-building';

export default function SkyHighBuilding(sqft, floors) {
    const building = new Building(sqft);
    return {
        ...building,
        _sqft: building.sqft,
        _floors: floors,
        get sqft() {
            return this._sqft;
        },
        get floors() {
            return this._floors;
        },
        evacuationWarningMessage() {
            return `Evacuate slowly the ${this._floors} floors.`;
        }
    };
}
