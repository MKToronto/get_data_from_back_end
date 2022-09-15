import App from './App.svelte';

var app = new App({
	target: document.body,
	headers: {
        'Access-Control-Allow-Origin': '*' // or, e.g. replacing * by http://localhost:8000
    }
});
var stores;
export default app;