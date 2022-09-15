<script>
  import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink
  } from "sveltestrap";

  let isOpen = false;

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }
  import "smelte/src/tailwind.css";

  

  import Router from "svelte-spa-router";
  import Home from "./Home/Home.svelte";

</script>

<head>
  <!-- <link
    rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
  /> -->
  <link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
/>
<!-- <link
  rel="stylesheet"
  href='bootstrap.min.css'
/> -->
  <link
    href="https://fonts.googleapis.com/icon?family=Material+Icons"
    rel="stylesheet"
  />
  <!-- <link
  href="icon.css"
  rel="stylesheet"
/> -->
  <!-- <link
    type="text/javascript"
    src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.4.8/socket.io.min.js"
  />
  <link
  src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"
  /> -->
  <!-- <link src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"/>
  <link src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.4/socket.io.js" integrity="sha512-aMGMvNYu8Ue4G+fHa359jcPb1u+ytAF+P2SCb+PxrjCdO3n3ZTxJ30zuH39rimUggmTwmh2u7wvQsDTHESnmfQ==" crossorigin="anonymous"/> -->
</head>

<Navbar color="light" light expand="md">
  <NavbarBrand href="/">FastAPI and Svelte</NavbarBrand>
  <NavbarToggler on:click={() => (isOpen = !isOpen)} />
  <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
    <Nav class="ml-auto" navbar>
      <NavItem>
        <NavLink href="/#/">Home</NavLink>
      </NavItem>

    </Nav>
  </Collapse>
</Navbar>

<Router
  routes={{
    "/": Home,
  }}
/>

