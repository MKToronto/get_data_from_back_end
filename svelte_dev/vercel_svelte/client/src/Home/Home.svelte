<script>
  import { onMount, onDestroy } from "svelte";
  import { value_to_send } from "./stores.js";
  let get_value_to_send_interval;
  onMount(async () => {
    get_global_values();
    get_value_to_send();
    make_new_get_value_to_send_interval(100);
    get_global_values();
  });

  onDestroy(() => {
    clearInterval(get_value_to_send_interval);
    console.log("destroyed get_value_to_send_interval");
  });

  async function get_value_to_send() {
    const response = await fetch(
      "https://get-data-python.vercel.app/get_value_to_send"
    );
    const get_value_to_send_response = await response.json();
    $value_to_send = get_value_to_send_response.value_to_send;
  }
  import { Slider } from "smelte";

  // async function send_time_sleep_to_back_end(slider_value_back_end){
  //   console.log("send_time_sleep_to_back_end", slider_value_back_end)
  //   const response = await fetch("https://get-data-python.vercel.app/send_time_sleep_to_back_end/"+slider_value_back_end);
  //   const get_value_to_send_response = await response.json();

  // }

  async function send_slider_choice_to_back_end(slider_choice) {
    console.log("send_slider_choice_to_back_end", slider_choice);
    const response = await fetch(
      "https://get-data-python.vercel.app/send_slider_choice_to_back_end/" +
        slider_choice
    );
    const send_slider_choice_to_back_end_response = await response.json();
  }

  async function get_global_values() {
    console.log("get_global_values");
    const response = await fetch(
      "https://get-data-python.vercel.app/get_global_values"
    );
    const get_global_values_resp = await response.json();
    slider_choice = get_global_values_resp.slider_choice;
  }

  async function make_new_get_value_to_send_interval(slider_value_front_end) {
    console.log("make_new_get_value_to_send_interval", slider_value_front_end);
    clearInterval(get_value_to_send_interval);
    get_value_to_send_interval = setInterval(function () {
      get_value_to_send();
    }, slider_value_front_end);
  }

  // let slider_value_back_end;
  // $: slider_value_back_end = 100;

  let slider_value_front_end;
  $: slider_value_front_end = 100;

  let slider_choice;
  $: slider_choice = "";
  // let value2 = 0;
  let disabled = false;
</script>

<div class="mt-20">
  <div class="grid grid-cols-12 gap-x-2 gap-y-16">
    <div class="col-start-2 col-end-12 text-center ">
      <p class="text-2xl">Welcome to a really great FastAPI and Svelte demo!</p>
    </div>
    <div class="col-start-2 col-end-12 text-center">
      <p class="text-2xl">Value Received From FastAPI:</p>
    </div>
    <div class="col-span-2 col-end-12 text-left">
      <p class="text-blue-400 text-2xl">{$value_to_send}</p>
    </div>
  </div>
</div>
<div class="mt-10">
  <div class="grid grid-cols-12 gap-1">
    <div class="col-start-2 col-end-12 text-center mb-2 ">
      <h6>Choose a character type:</h6>
    </div>
    <div class="col-start-2 col-end-12 text-center mb-2 ">
      <div class=" flex justify-center ">
        <div class="text-center">
          <!-- <div class="col-start-2 col-span-3 text-right"> -->
          <label>
            <input
              bind:group={slider_choice}
              on:change={send_slider_choice_to_back_end(slider_choice)}
              type="radio"
              value="Digits"
            />
            <h6>Digits</h6>
          </label>
        </div>
        <div class="text-center">
          <label>
            <input
              bind:group={slider_choice}
              on:change={send_slider_choice_to_back_end(slider_choice)}
              type="radio"
              value="Letters"
            />
            <h6>Letters</h6>
          </label>
        </div>
        <div class="text-center">
          <label>
            <input
              bind:group={slider_choice}
              on:change={send_slider_choice_to_back_end(slider_choice)}
              type="radio"
              value="Punctuation"
            />
            <h6>Punctuation</h6>
          </label>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="mt-10 mb-20">
  <div class="grid grid-cols-12 gap-y-2">
    <div class="col-start-2 col-end-12 text-center">
      <h6>Number of Milliseconds Between Updates:</h6>
    </div>
    <div class="col-start-2 col-end-12 text-center">
      <small>Value: {slider_value_front_end}</small>
    </div>
    <div class="col-start-4 col-span-6 ">
      <Slider
        min="100"
        max="2000"
        color="blue"
        bind:value={slider_value_front_end}
        {disabled}
        on:change={() =>
          make_new_get_value_to_send_interval(slider_value_front_end)}
      />
    </div>
  </div>
</div>
