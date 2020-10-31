import LoginForm from './LoginForm';
import {compose} from 'redux';
import {connect} from 'react-redux';
import {login} from '../../redux/reducers/auth_reducer';
import {reduxForm} from 'redux-form';

const mapDispatchToProps = state => ({
  user: state.auth.user,
});

export default compose(
  connect(mapDispatchToProps, {login}),
  reduxForm({form: 'login'})
)(LoginForm);