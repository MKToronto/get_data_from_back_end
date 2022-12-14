import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
import json from '@rollup/plugin-json'
import sveltePreprocess from 'svelte-preprocess';




const production = !process.env.ROLLUP_WATCH;
const smelte=require("smelte/rollup-plugin-smelte");

export default {
	input: 'src/main.js',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: 'public/build/bundle.js'
	},
	plugins: [
		svelte({
			// enable run-time checks when not in production
			dev: !production,
			// we'll extract any component CSS out into
			// a separate file — better for performance
			css: css => {
				css.write('bundle.css');
			},
			preprocess: sveltePreprocess()
    		}),
			resolve({
			browser: true,
			dedupe: importee => importee === 'svelte' || importee.startsWith('svelte/')
		}),
		
		
		smelte({ 
			purge: production,
			output: "global.css", // it defaults to static/global.css which is probably what you expect in Sapper 
			postcss: [], // Your PostCSS plugins
			whitelist: [], // Array of classnames whitelisted from purging
			whitelistPatterns: [], // Same as above, but list of regexes
			tailwind: { 
			  colors: { 
				primary: "#b027b0",
				secondary: "#009688",
				error: "#f44336",
				success: "#4caf50",
				alert: "#ff9800",
				blue: "#2196f3",
				dark: "#212121" 

			  }, // Object of colors to generate a palette from, and then all the utility classes
			  darkMode: true, 
			}, 
			// Any other props will be applied on top of default Smelte tailwind.config.js
		  }),
		
		json({
			  compact: true
			}),

		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration —
		// consult the documentation for details:
		// https://github.com/rollup/rollup-plugin-commonjs
		resolve({
			browser: true,
			dedupe: importee => importee === 'svelte' || importee.startsWith('svelte/')
		}),
		commonjs(),
		
		// Watch the `public` directory and refresh the
		// browser on changes when not in production
		!production && livereload('public'),
		// !production && terser(),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser() 
	],
	watch: {
		clearScreen: false
	}
};
