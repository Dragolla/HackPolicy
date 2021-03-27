import { AppBar, Toolbar } from '@material-ui/core'
import './App.css'

const Header = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <img src="./logo.svg" alt="Logo" height="25" width="25" />
      </Toolbar>
    </AppBar>
  )
}

export default Header
