<script>
  import { onMount, onDestroy } from "svelte";
  import { value_to_send } from "./stores.js";
  let get_value_to_send_interval;
  onMount(async () => {
    get_value_to_send();
    make_new_get_value_to_send_interval(50)
  });

  onDestroy(() => {
    clearInterval(get_value_to_send_interval);
    console.log("destroyed get_value_to_send_interval");
  });

  async function get_value_to_send() {
    const response = await fetch("https://vnk5v6.deta.dev/get_value_to_send");
    const get_value_to_send_response = await response.json();
    $value_to_send = get_value_to_send_response.value_to_send;
  }
  import {
    Slider,
  } from "smelte";

  async function send_time_sleep_to_back_end(slider_value_back_end){
    console.log("send_time_sleep_to_back_end", slider_value_back_end)
    const response = await fetch("https://vnk5v6.deta.dev/send_time_sleep_to_back_end/"+slider_value_back_end);
    const get_value_to_send_response = await response.json();


  }

  async function make_new_get_value_to_send_interval(slider_value_front_end){
    console.log("make_new_get_value_to_send_interval", slider_value_front_end)
    clearInterval(get_value_to_send_interval);
    get_value_to_send_interval = setInterval(function () {
      get_value_to_send();
    }, slider_value_front_end);


  }

  let slider_value_back_end;
  $: slider_value_back_end = 1

  let slider_value_front_end;
  $: slider_value_front_end = 1
  // let value2 = 0;
  let disabled = false;

</script>

<div class="mt-20">
  <div class="grid grid-cols-12 gap-y-20">
    <div class="col-start-4 col-end-10  ">
      <p class="text-2xl">Welcome to a really great FastAPI and Svelte demo!</p>
    </div>
    <div class="col-start-5 col-end-8 ">
      
      <p class="text-2xl">Value Received From FastAPI:</p>
    </div>
      <div class="col-start-8 col-end-9 ">
      <p class="text-blue-400 text-2xl">{$value_to_send}</p>
    </div>
    <div class="col-start-4 col-end-10 ">

<h6>Number of Milliseconds Between Updates On <u> FastAPI Backend </u></h6>

<small>Value: {slider_value_back_end}</small>

<Slider min="500" max="3000" color="blue" bind:value={slider_value_back_end} {disabled} on:change={() => send_time_sleep_to_back_end(slider_value_back_end)} />



    </div>
    <div class="col-start-4 col-end-10 ">

      <h6>Number of Milliseconds Between Updates From <u>Svelte Front End</u> </h6>
      
      <small>Value: {slider_value_front_end}</small>
      
      <Slider min="500" max="3000" color="blue" bind:value={slider_value_front_end} {disabled} on:change={() => make_new_get_value_to_send_interval(slider_value_front_end)} />
      
      
      
          </div>
  </div>
    </div>




    
