import {
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  makeStyles,
} from '@material-ui/core'
import './App.css'

const useStyle = makeStyles({
  titleText: {
    margin: '10px',
  },
})

const Header = () => {
  const classes = useStyle()
  return (
    <AppBar position="static">
      <Toolbar>
        <IconButton aria-label="AppIcon">
          <img src="https://svgur.com/i/VVY.svg" alt="Logo" width="50" />
        </IconButton>
        <Typography variant="h4" className={classes.titleText}>
          Viridi
        </Typography>
      </Toolbar>
    </AppBar>
  )
}

export default Header
