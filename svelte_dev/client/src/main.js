import App from './App.svelte';

var app = new App({
	target: document.body,
	headers: {
        'Access-Control-Allow-Credentials': 'true',
		'Access-Control-Allow-Origin': '*',
		'Access-Control-Allow-Methods': 'GET,OPTIONS,PATCH,DELETE,POST,PUT',
		'Access-Control-Allow-Headers': 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version',    }
});
var stores;
export default app;