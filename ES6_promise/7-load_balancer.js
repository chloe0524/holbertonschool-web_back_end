/*eslint-disable*/
export default (chinaDownload, USDownload) => Promise.race([chinaDownload, USDownload]).then((result) => result);